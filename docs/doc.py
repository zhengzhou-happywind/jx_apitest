BASE_URL = "http://127.0.0.1:8000/api/v1"
TEST_LIST = [
    {
        "name": "API信息",
        "url": "/",
        "method": "get",
        "response":
            """
            {
              "version": "1.0.1",
              "config": {
                "network_id": "51687",
                "rpc_server": "https://mainnet.infura.io/llyrtzQ3YhkdESt2Fzrk",
                "cc": 324
              }
            }
            """
    },
]
