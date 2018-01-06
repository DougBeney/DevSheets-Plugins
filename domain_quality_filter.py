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

    def domainQualityAction(self, e):
        userinput = self.getDialog("Domain Quality Filter", "What column holds your URLS?")
        if userinput:
            url_col = int(self.col2num(userinput)) - 1
            if url_col == None or url_col < 0:
                self.gui.showMessage("Failure", "Can't run filter. Please make sure you've provided proper input.")
            else:
                newSheetObject = []

                sheetObject = self.gui.sheetObject

                for row in sheetObject:
                    if not self.contains_bad_pattern(row[url_col]):
                        newSheetObject.append(row)

                self.gui.sheetObject = newSheetObject.copy()
                self.gui.update_sheet()

    def init(self):
        self.createMenuItem(self.gui.menu_filter, "Domain Quality", self.domainQualityAction)

settings = {
    "class": DomainQuality,
    'name': "Domain Quality Filter",
    'version': "0.0.1",
}

