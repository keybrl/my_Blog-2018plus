import markdown

base_info = {
    'title': 'KeybrL\'s Blog',
    'generator': 'MkDocs v1.0.3',
    'link': 'https://blog.keybrl.com/',
    'author_name': 'KeybrL',
    'author_email': 'keyboard-l@outlook.com',
    'rights': 'Copyright &amp;copy; &lt;a href="https://blog.keybrl.com/">KeybrL&lt;/a> All Rights Reserved.',
    'updated': '2018-11-19T00:00:01+08:00'
}

entrys = [
    {
        'title': '软路由与NAS 硬件平台搭建',
        'link': 'http://blog.keybrl.com/boring/2018-11-02-router1_hardware/',
        'updated': '2018-11-18T00:00:00+08:00',
        'published': '2018-11-18T00:00:00+08:00',
        'summary': '',
        'content_url': './posts/2018-11-02-router1_hardware.md'
    },
    {
        'title': 'Windows 常用注册表项',
        'link': 'https://blog.keybrl.com/posts/2018-10-23-Windows-regedit/',
        'updated': '2018-10-23T00:00:00+08:00',
        'published': '2018-10-23T00:00:00+08:00',
        'summary': '',
        'content_url': './posts/2018-10-23-Windows-regedit.md'
    },
    {
        'title': 'keybrl-mines - 优雅的扫雷从此无处不在',
        'link': 'https://blog.keybrl.com/projects/2018-10-14-Project-keybrl-gnome/',
        'updated': '2018-10-14T00:00:01+08:00',
        'published': '2018-10-14T00:00:01+08:00',
        'summary': '',
        'content_url': './posts/2018-10-14-Project-keybrl-gnome.md'
    },
    {
        'title': 'Nginx常用配置套路',
        'link': 'https://blog.keybrl.com/posts/2018-07-02-nginx-configure/',
        'updated': '2018-07-02T00:00:01+08:00',
        'published': '2018-07-02T00:00:01+08:00',
        'summary': '',
        'content_url': './posts/2018-07-02-nginx-configure.md'
    },
    {
        'title': '通过MkDocs搭建个人博客',
        'link': 'https://blog.keybrl.com/posts/2018-05-19-mkdocs-blog/',
        'updated': '2018-05-19T00:00:01+08:00',
        'published': '2018-05-19T00:00:01+08:00',
        'summary': '',
        'content_url': './posts/2018-05-19-mkdocs-blog.md'
    }
]

exts = [
    'markdown.extensions.extra',
    'markdown.extensions.codehilite',
    'markdown.extensions.admonition',
    'markdown.extensions.tables',
    'markdown.extensions.sane_lists',
    'markdown.extensions.nl2br',
    'markdown.extensions.meta',
    'markdown.extensions.toc'
]

feed_xml = '''<?xml version="1.0" encoding="utf-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">
    <title type="text">{title}</title>
    <generator>{generator}</generator>
    <id>{link}</id>
    <link href="{link}" rel="alternate" type="text/html"/>
    <link href="{link}feed.xml" rel="self" type="application/rss+xml"/>
    <author>
        <name>{author_name}</name>
        <email>{author_email}</email>
    </author>
    <rights type="html">{rights}</rights>
    <updated>{updated}</updated>
'''.format(
        title=base_info['title'],
        generator=base_info['generator'],
        link=base_info['link'],
        author_name=base_info['author_name'],
        author_email=base_info['author_email'],
        rights=base_info['rights'],
        updated=base_info['updated']
    )

for entry in entrys:
    content_md = ''
    with open(entry['content_url'], 'r', encoding='utf-8') as file:
        content_md = file.read()
    content_html = markdown.markdown(content_md, extensions=exts)
    content_html = content_html.replace('&', '&amp;')
    content_html = content_html.replace('<', '&lt;')

    content = content_html

    feed_xml += '''
    <entry>
        <title>{title}</title>
        <link rel="alternate" type="text/html" title="{title}" href="{link}"/>
        <id>{link}</id>
        <updated>{updated}</updated>
        <published>{published}</published>
        <summary>{summary}</summary>
        <content type="html" xml:base="{link}">{content}</content>
    </entry>
'''.format(
        title=entry['title'],
        link=entry['link'],
        published=entry['published'],
        updated=entry['updated'],
        summary=entry['summary'],
        content=content
    )

feed_xml += '</feed>\n'

with open('feed.xml', 'w', encoding='utf-8') as file:
    file.write(feed_xml)
