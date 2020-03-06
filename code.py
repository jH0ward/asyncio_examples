import aiohttp
import time
import requests
import asyncio
from bs4 import BeautifulSoup
from aiohttp import ClientSession


def time_print(s):
    print(f'{s} at {time.strftime("%X")}')


def C(r):
    html = r.decode("utf-8")
    #soup = BeautifulSoup(html, 'html.parser')
    return html
    #val=soup.title.text
    #return val


async def wraps_hello(wiki_url):
    res = await hello(wiki_url)
    return C(res)


async def hello(url):
    async with ClientSession() as session:
        async with session.get(url) as response:
            response = await response.read()
            return response


def hello_sync(url):
    r = requests.get(url)
    html = r.text
    #soup = BeautifulSoup(html, 'html.parser')
    #val=soup.title.text
    #return val
    return html


us_states = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado",
  "Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois",
  "Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland",
  "Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana",
  "Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York",
  "North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania",
  "Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah",
  "Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]


async def run_main():
    start = time.time()
    time_print("Beginning loop")
    tasks = []
    wiki_template = 'https://en.wikipedia.org/wiki/replaceme'
    for i in range(50):
        wiki_url = wiki_template.replace('replaceme', us_states[i])
        task = asyncio.ensure_future(
            wraps_hello(wiki_url))

        # In the callback, set the task value to what you want
        tasks.append(task)

    await asyncio.gather(*tasks)

    #for t in tasks:
    #    print(t.result())

    time_print("Ending async loop")
    end = time.time()
    print(f'Async took {end-start} seconds')


if __name__ == '__main__':
    asyncio.run(run_main())
    start = time.time()
    for i in range(50):
        wiki_template = 'https://en.wikipedia.org/wiki/replaceme'
        wiki_url = wiki_template.replace('replaceme', us_states[i])
        r = hello_sync(wiki_url)
        #print(r)
    end = time.time()
    print(f'Sync took {end-start} seconds')
