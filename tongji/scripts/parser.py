import bs4


html_path = 'html/honor.html'

def parse_honor(html_path, keywords=None):
    """
    Find class="count", which contains many <div> elements with class="list",
    each containing <img> <div class="list_count_title> <div class="list_desc">.
    Return another format like:
        <div class="honor-card">
            <div class="icon-container">
                <img src="https://example.com/icon.png" alt="Icon" class="icon">
            </div>
            <div class="honor-details">
                <div class="award-title">XXXXXXXXXXXXXX</div>
                <div class="authors">XXX, XXX, XXX, XXX, XXX</div>
            </div>
        </div>
    """
    with open(html_path, 'r', encoding='utf-8') as file:
        html = file.read()

    soup = bs4.BeautifulSoup(html, 'html.parser')
    count_div = soup.find('div', class_='count')
    if not count_div:
        return []

    honor_list = []
    for item in count_div.find_all('div', class_='list'):
        img = item.find('img')['src'] if item.find('img') else ''
        title = item.find('div', class_='list_count_title').get_text(strip=True) if item.find('div', class_='list_count_title') else ''
        desc = item.find('div', class_='list_desc').get_text(strip=True) if item.find('div', class_='list_desc') else ''

        if keywords:
            if not any(keyword in desc for keyword in keywords):
                continue
        
        honor_list.append({
            'img': img,
            'title': title,
            'desc': desc
        })
        
        output_html = ''
        for honor in honor_list:
            output_html += f"""
            <div class="honor-card">
                <div class="icon-container">
                    <img src="{honor['img']}" alt="Icon" class="icon">
                </div>
                <div class="honor-details">
                    <div class="award-title">{honor['title']}</div>
                    <div class="authors">{honor['desc']}</div>
                </div>
            </div>
            """
    return output_html.strip()



print(parse_honor(html_path, ['Jingkuan Song', 'Heng Tao Shen', '']))
