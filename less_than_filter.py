from dougsheets import plugin


class LessThan(plugin.Plugin):
    def removeLessThan(self, col, number):
            newSheetObject = []
            sheetObject = self.gui.sheetObject

            for row in sheetObject:
                if type(row[col]) == str:
                    newSheetObject.append(row)
                else:
                    if int(row[col]) >= number:
                        newSheetObject.append(row)

            self.gui.sheetObject = newSheetObject
            self.gui.update_sheet()

    def LessThanAction(self, e):
        number = self.getInput__Variable('num', "Less-Than Filter", "Under what number should we filter out?", e)
        column = self.getInput__Column('col', "Less-Than Filter", "What column should we filter from?", e)

        if number and column:
            number = int(number)
            self.removeLessThan(column, number)

    def init(self):
        self.createMenuItem(
            self.gui.menu_filter,
            "Less Than",
            self.LessThanAction,
            cli_help="Usage: 'less_than col=[COLUMN LETTER/NUMBER] num=[NUMBER]'"
        )

settings = {
    "class": LessThan,
    'name': "Less-Than Filter",
}

