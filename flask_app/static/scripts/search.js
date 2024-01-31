$(function () {

    const searchInput = $("#searchInput");
    const itemsDiv = $("#searchResults");
    $(searchInput).keypress((key) => key.keyCode == 13 ? getItems(): null);
    $("#searchButton").click(() => getItems());
    $("#orderBy").change(() => orderItems());
    $("#displayOrder").change(() => displayOrder());
    $("#filterBy").change(() => filterItems());
    getItems();

    function getItems () {
        let name = searchInput.val().toLowerCase();
        let searchLink = "http://localhost:5000/api/v1/search/";

        $.ajax({
            type: "GET",
            url: searchLink + name,
            success: function (data) {
                itemsDiv.empty(); // clear the previous search items
                const keys = Object.keys(data)
                keys.forEach((key, index) => {
                    const item = data[key];
                    const itemVendor = item["vendor"];
                    const itemLink = item["link"];
                    const imgUrl = item["img_link"];
                    const itemName = item["name"];
                    const itemPrice = item["price"];
                    const article = $([
                        `<article class='ItemCard' vendor=${itemVendor.toLowerCase()} id=''>`,
                        "    <a class='ItemLink' href='" + itemLink + "'>",
                        "        <div class='ItemImage'>",
                        "            <img src=" + imgUrl + " alt='Image of " + itemName + "'>",
                        "        </div>",
                        "        <div class='ItemInfo'>",
                        "            <div class='ItemName'>" + itemName + "</div>",
                        "            <div>From&nbsp;<span class='ItemVendor'>" + itemVendor + "</span></div>",
                        "            <div>KSH&nbsp;<span class='ItemPrice'>" + itemPrice + "</span></div>",
                        "        </div>",
                        "    </a>",
                        "</article>"
                    ].join('\n'));
                    if (index === 1) {
                        console.log(article);
                    }
                    itemsDiv.append(article);
                })
                orderItems();
                filterItems();
            },
            fail: function (error) { console.log(error) }
        })
    }
    function orderItems () {
        const orderVal = $("#orderBy").val();
        const sortedItems = $(".ItemCard").sort(function (a, b) {
            const v1 = $(a).find(`.${orderVal}`).text();
            const v2 = $(b).find(`.${orderVal}`).text();
            if (orderVal == "ItemPrice") {
                const p1 = v1.replace(",", "");
                const p2 = v2.replace(",", "");
                return parseInt(p1) - parseInt(p2);
            }
            if (v1 < v2) {
                return -1;
            }
            if (v1 == v2) {
                return 0;
            }
            return 1;
        });
        itemsDiv.empty();
        itemsDiv.append(sortedItems);
        $("#displayOrder").val("0")
    }
    function displayOrder () {
        const items = $(itemsDiv).find(".ItemCard");
        itemsDiv.empty();
        itemsDiv.append(items.toArray().reverse());
    }
    function filterItems () {
        const filterVal = $("#filterBy").val().toLowerCase();
        if (filterVal == "none") {
            $(itemsDiv).find('.ItemCard').css("display", "flex")
            return;
        }
        $(itemsDiv).find('.ItemCard').css("display", "none")
        $(itemsDiv).find(`[vendor="${filterVal}"]`).css("display", "flex")
    }
})
