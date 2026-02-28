import json

'''
Dans la console du navigateur

console.log(JSON.stringify($('.chapter-task-row').find('.chapter-item-title > a').map(function () {
    const $el = $(this)
    const href = $el.attr('href').split('.php?')[1]
    const title = $el.text()
    return { href, title }
}).toArray()))

'''

"coller le résultat ici"
tasks = [{"href":"idChapter=649&idTask=2051","title":"1) Département de médecine : contrôle d'une épidémie"},{"href":"idChapter=649&idTask=2057","title":"2) Administration : comptes annuels"},{"href":"idChapter=649&idTask=2053","title":"3) Département de pédagogie : le « c'est plus, c'est moins »"},{"href":"idChapter=649&idTask=2052","title":"4) Département d'architecture : construction d'une pyramide"},{"href":"idChapter=649&idTask=2058","title":"5) Département de chimie : mélange explosif"}]

for task in tasks:
    href = task["href"]
    title = task["title"]
    print(title)
    print(len(title) * '=')
    print()
    print(f"..  activecode:: {href}")
    print()

