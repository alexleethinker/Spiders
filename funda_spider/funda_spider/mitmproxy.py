import re  
from mitmproxy import ctx  
    
def response(flow):  
  """修改应答数据 
  """  
  if '/js/dwswscsvwabwrdwvwuaqsf.' in flow.request.url:  
      flow.response.text = flow.response.text.replace("webdriver", "false")
      flow.response.text = flow.response.text.replace("isWebdriver", "false")