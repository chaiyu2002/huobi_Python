class OrderHistoryItem:
    """
    The result of batch cancel operation.

    :member
        orderOrigTime
        lastActTime
        symbol
        source
        orderSide
        orderType
        timeInForce
        clientOrderId
        accountId
        orderPrice
        orderSize
        stopPrice
        orderStatus

    """

    def __init__(self):
        self.orderOrigTime = ""
        self.lastActTime = ""
        self.symbol = ""
        self.source = ""
        self.orderSide = ""
        self.orderType = ""
        self.timeInForce = ""
        self.clientOrderId = ""
        self.accountId = ""
        self.orderPrice = ""
        self.orderSize = ""
        self.stopPrice = ""
        self.orderStatus = ""
        self.orderId = ""
        self.orderValue = ""
        self.trailingRate = ""
        self.orderCreateTime = ""
        self.errCode = ""
        self.errMessage = ""

    def print_object(self, format_data=""):
        from huobi.utils.print_mix_object import PrintBasic
        PrintBasic.print_basic("self.orderOrigTime: " + str(self.orderOrigTime), format_data + "")
        PrintBasic.print_basic("self.lastActTime: " + str(self.lastActTime), format_data + "")
        PrintBasic.print_basic("self.symbol: " + str(self.symbol), format_data + "")
        PrintBasic.print_basic("self.source: " + str(self.source), format_data + "")
        PrintBasic.print_basic("self.orderSide: " + str(self.orderSide), format_data + "")
        PrintBasic.print_basic("self.orderType: " + str(self.orderType), format_data + "")
        PrintBasic.print_basic("self.timeInForce: " + str(self.timeInForce), format_data + "")
        PrintBasic.print_basic("self.clientOrderId: " + str(self.clientOrderId), format_data + "")
        PrintBasic.print_basic("self.accountId: " + str(self.accountId), format_data + "")
        PrintBasic.print_basic("self.orderPrice: " + str(self.orderPrice), format_data + "")
        PrintBasic.print_basic("self.orderSize: " + str(self.orderSize), format_data + "")
        PrintBasic.print_basic("self.stopPrice: " + str(self.stopPrice), format_data + "")
        PrintBasic.print_basic("self.orderStatus: " + str(self.orderStatus), format_data + "")
        PrintBasic.print_basic("self.orderId: " + str(self.orderId), format_data + "")
        PrintBasic.print_basic("self.orderValue: " + str(self.orderValue), format_data + "")
        PrintBasic.print_basic("self.trailingRate: " + str(self.trailingRate), format_data + "")
        PrintBasic.print_basic("self.orderCreateTime: " + str(self.orderCreateTime), format_data + "")
        PrintBasic.print_basic("self.errCode: " + str(self.errCode), format_data + "")
        PrintBasic.print_basic("self.errMessage: " + str(self.errMessage), format_data + "")
