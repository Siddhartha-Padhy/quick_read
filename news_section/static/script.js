function saveArticle(ind) {
  let title = document.getElementById(`headline${ind}`).textContent.trim()
  let url = document.getElementById(`url${ind}`).href

  if (localStorage['Saved'] != null) {
    let prev = JSON.parse(localStorage['Saved'])
    prev[title] = url
    localStorage['Saved'] = JSON.stringify(prev)
  } else {
    let store = { [title]: url }
    store = JSON.stringify(store)
    localStorage['Saved'] = store
  }
}

function delete_article(ind) {
  let article = document.getElementById(`article${ind}`).textContent.trim()
  console.log(article)
  let data = JSON.parse(localStorage['Saved'])
  console.log(data)
  delete data[article]
  console.log(data)
  localStorage['Saved'] = JSON.stringify(data)
  get_saved_articles()
}

function get_saved_articles() {
  let saved_section = document.getElementById('saved-articles')
  if (saved_section != null) {
    document.getElementById('saved-articles').innerHTML = ''
    if (localStorage['Saved'] != null) {
      let articles = JSON.parse(localStorage['Saved'])
      let count = 0
      for (article in articles) {
        saved_section.innerHTML += `<div class="list-group-item list-group-item-action d-flex justify-content-between">
        <a href=${articles[article]} class="card-link" id="article${count}">
          ${article}
        </a>
        <button class="btn btn-danger custom-delete-btn" id="del-btn${count}" onclick="delete_article(${count++})">
          <i class="fa fa-trash" aria-hidden="true"></i>
        </button>
      </div>`
      }
    } else {
      saved_section.innerHTML += `<a href="#" class='list-group-item list-group-item-action'>Save some articles to see them here.</a>`
    }
  }
}
