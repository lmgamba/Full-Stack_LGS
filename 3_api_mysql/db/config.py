import aiomysql

async def get_connection():
    return await aiomysql.connect(
        host="172.22.224.1",
        port=3306,
        user="wsl_root",
        password="Targaryen*27",
        db="202509_shop"
    )

    
    
