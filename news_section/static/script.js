function saveArticle(ind) {
  console.log(ind)
  let title = document.getElementById(`headline${ind}`).textContent.trim()
  let url = document.getElementById(`url${ind}`).href

  if (localStorage['Saved'] != null) {
    let prev = JSON.parse(localStorage['Saved'])
    prev[title] = url
    localStorage['Saved'] = JSON.stringify(prev)
  } else {
    let store = { [title]: url }
    store = JSON.stringify(store)
    console.log(store)
    localStorage['Saved'] = store
  }
}

// function get_saved_articles() {
//   console.log('Working')
// }

let saved_section = document.getElementById('saved-articles')

if (saved_section != null) {
  if (localStorage['Saved'] != null) {
    let articles = JSON.parse(localStorage['Saved'])
    for (article in articles) {
      saved_section.innerHTML += `<div class="list-group-item list-group-item-action d-flex justify-content-between">
      <a href=${articles[article]} class="card-link">
        ${article}
      </a>
      <button class="btn btn-danger custom-delete-btn">
        <i class="fa fa-trash" aria-hidden="true"></i>
      </button>
    </div>`
    }
  } else {
    saved_section.innerHTML += `<a href="#" class='list-group-item list-group-item-action'>Save some articles to see them here.</a>`
  }
}
