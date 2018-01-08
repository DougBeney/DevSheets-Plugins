import re
from dougsheets import plugin


class RootDomainRemove(plugin.Plugin):
    def RemoveRootDomains(self, col):
            newSheetObject = []
            sheetObject = self.gui.sheetObject

            for row in sheetObject:
                regex = r'^(https?://)?[\w\.\-\_\$\#\@\%]+\/.+'
                regex_matches = len(re.findall(regex, row[col]))
                if regex_matches > 0:
                    newSheetObject.append(row)

            self.gui.sheetObject = newSheetObject
            self.gui.update_sheet()

    def Action(self, e):
        column = self.getInput__Column('col', "Root Domain Removal", "What column should we filter from?", e)
        self.RemoveRootDomains(column)

    def init(self):
        self.createMenuItem(
            self.gui.menu_filter,
            "Remove Root Domains",
            self.Action,
        )

settings = {
    "class": RootDomainRemove,
    'name': "Root Domain Remove"
}

