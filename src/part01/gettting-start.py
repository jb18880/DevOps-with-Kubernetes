import uuid
import time
from datetime import datetime

# 生成随机字符串
random_string = str(uuid.uuid4())

# 输出每5秒一次
while True:
    # 获取当前时间戳
    timestamp = datetime.utcnow().isoformat() + 'Z'
    
    # 打印时间戳和随机字符串
    print(f"{timestamp}: {random_string}")
    
    # 等待5秒
    time.sleep(5)

