

$('#test').text(function (i, text)
{
    return text.replace('&lt;', '<').replace('&gt;', '>');
});

