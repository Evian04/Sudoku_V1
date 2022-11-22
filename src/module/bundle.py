class Bundle:
    """ Packages the information returned by the check function. """

    def __init__(self, isFull: bool, isError: bool, formatsErrors: list[str] = [], idErrors: list[int] = [], doubloonDigitErrors: list[str] = []) -> None:
        self.isFull: bool = isFull
        self.isError: bool = isError
        self.formatsErrors: list[str] = formatsErrors
        self.idErrors: list[int] = idErrors
        self.doubloonDigitErrors: list[str] = doubloonDigitErrors

        if not (len(formatsErrors) == len(idErrors) and len(idErrors) == len(doubloonDigitErrors)):
            print("Error class package : lists's length aren't equals")
