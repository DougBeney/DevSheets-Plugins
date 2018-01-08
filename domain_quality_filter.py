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

    def removeBadDomains(self, url_col):
        newSheetObject = []
        sheetObject = self.gui.sheetObject

        for row in sheetObject:
            if not self.contains_bad_pattern(row[url_col]):
                newSheetObject.append(row)

        self.gui.sheetObject = newSheetObject.copy()
        self.gui.update_sheet()


    def domainQualityAction(self, e):
        column = self.getInput__Column('col', "Domain Quality Filter", "What column should we filter from?", e)
        self.removeBadDomains(column)

    def init(self):
        self.createMenuItem(self.gui.menu_filter, "Domain Quality", self.domainQualityAction)

settings = {
    "class": DomainQuality,
    'name': "Domain Quality Filter",
    'version': "0.0.1",
}
