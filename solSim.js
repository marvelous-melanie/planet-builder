$("#starRadio").onclick(() => {
    console.log("onclick is running");
    $("body_setup").append(
        " <form>\n" +
        "            <input type = \"text\" name = \"\">Name<br>\n" +
        "            <input type = \"text\" name = \"\">Mass<br>\n" +
        "            <input type = \"text\" name = \"\">Radius<br>\n" +
        "            <input type = \"text\" name = \"\">Temperature<br>\n" +
        "        </form>\n"
    )
})