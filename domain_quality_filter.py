from dougsheets import plugin


class DomainQuality(plugin.Plugin):
    bad_patterns = [
        "blogspot",
        "wordpress.com",
        "weebly.com",
        "wix.com",
        ".shopify.com"
    ]

    def contains_bad_pattern(self, string):
        for pattern in self.bad_patterns:
            if pattern in str(string):
                return True
        return False

    def promptUser4Col(self, title, text):
        userinput = self.getDialog(title, text)
        if userinput:
            url_col = self.col2num(userinput) - 1
            if url_col == None or url_col < 0:
                return None
            else:
                return url_col
        else:
            return None

    def removeUnder10(self):
        url_col = self.promptUser4Col("Filter out <= 10", "What column should we filter out under-10s?")
        if url_col:
            newSheetObject = []

            sheetObject = self.gui.sheetObject

            for row in sheetObject:
                if type(row[url_col]) == str:
                    newSheetObject.append(row)
                else:
                    if int(row[url_col]) >= 10:
                        newSheetObject.append(row)

            self.gui.sheetObject = newSheetObject.copy()
            self.gui.update_sheet()

    def removeBadDomains(self):
        url_col = self.promptUser4Col("Domain Quality Filter", "What column holds your URLS?")
        if url_col:
            newSheetObject = []

            sheetObject = self.gui.sheetObject

            for row in sheetObject:
                if not self.contains_bad_pattern(row[url_col]):
                    newSheetObject.append(row)

            self.gui.sheetObject = newSheetObject.copy()
            self.gui.update_sheet()

    def domainQualityAction(self, e):
        self.removeBadDomains()
        self.removeUnder10()

    def init(self):
        self.createMenuItem(self.gui.menu_filter, "Domain Quality", self.domainQualityAction)

settings = {
    "class": DomainQuality,
    'name': "Domain Quality Filter",
    'version': "0.0.1",
}

