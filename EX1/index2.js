let elList = document.querySelector(".list")

function renderArr(arr, List) {
    arr.map(item => {
        let newDiv = document.createElement("div")
        let newImg = document.createElement("img")
        let newCategory = document.createElement("category")
        let newprice = document.createElement("price")

        newDiv.classList.add("card")


        newImg.src = item.image
        newCategory.textContent =  item.category
        newprice.textContent = item.price


        newImg.style = width = "50%"
        elList.appendChild(newDiv)
        newDiv.appendChild(newImg)
        newDiv.appendChild(newCategory)
        newDiv.appendChild(newprice)
    })
}

fetch("https://fakestoreapi.com/products")
    .then(res => res.json())
    .then(users => renderArr(users))