class Bundle:
    """ Packages the information returned by the check function. """

    def __init__(self, isConflicts: bool, formatsConflicts: list, idConflicts: list, doubloonDigitConflicts: list):
        self.isConflicts: bool = isConflicts
        self.formatsConflicts: list[str] = formatsConflicts
        self.idConflicts: list[int] = idConflicts
        self.doubloonDigitConflicts: list[str] = doubloonDigitConflicts

        if not (len(formatsConflicts) == len(idConflicts) and len(idConflicts) == len(doubloonDigitConflicts)):
            print("Error class package : lists's length aren't equals")