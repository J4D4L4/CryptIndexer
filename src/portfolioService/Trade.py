class trade:
    type=''
    text=''
    amt=0
    value=0
    symbol=''

    def __init__(self, iType, iText, iAmt,iValue,symbol):
        self.type=iType
        self.text=iText
        self.amt=iAmt
        self.value=iValue
        self.symbol=symbol