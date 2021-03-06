#############################################################
# 2016-09-26: ChildMessageType.py 
# Author: Jeremy M. Gibson (State Archives of North Carolina)
# 
# Description: Implementation of the ChildMessageType
##############################################################


class ChildMessage:
    """"""
    
    def __init__(self, ):
        """Constructor for ChildMessageType"""
        self.local_id = None  # type: int
        self.message_id = None  # type: MessageIdType
        self.headers = None  # type: [HeaderType]
