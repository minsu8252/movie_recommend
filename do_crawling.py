import crawling

from concurrent.futures import ThreadPoolExecutor # 비동기처리 = 순차적으로 실행 (동시 x)
from concurrent.futures import ProcessPoolExecutor # 비동기처리

page = 13323069

while page > 13321069 :
    page = str(page)
    url = f"http://movie.naver.com/movie/point/af/list.nhn?st=nickname&sword={page}&target=after"

    with ThreadPoolExecutor(max_workers=3) as executor:
        executor.submit(crawling.do_crawl, url)

        page = int(page)
        page -= 1