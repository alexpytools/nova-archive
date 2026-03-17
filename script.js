async function loadPosts(){

let res = await fetch("data/posts.json")
let posts = await res.json()

posts.sort((a,b)=> new Date(b.date)-new Date(a.date))

render(posts)

document.getElementById("search").addEventListener("input",e=>{

let q = e.target.value.toLowerCase()

let filtered = posts.filter(p =>
p.title.toLowerCase().includes(q) ||
p.desc.toLowerCase().includes(q) ||
p.tags.join(" ").toLowerCase().includes(q)
)

render(filtered)

})

}

function render(posts){

let container = document.getElementById("posts")
container.innerHTML=""

posts.forEach(p=>{

let card = document.createElement("div")
card.className="post-card"

card.onclick=()=>window.location=p.url

let tags = p.tags.map(t=>`<span class="tag">#${t}</span>`).join("")

card.innerHTML=`

<div class="post-title">${p.title}</div>
<div class="post-desc">${p.desc}</div>
<div class="post-date">${p.date}</div>
<div class="tags">${tags}</div>

`

container.appendChild(card)

})

}

loadPosts()