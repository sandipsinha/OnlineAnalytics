function removePopovers() {
    $('.popover').each(function() {
        $(this).remove();
    });
}

function showPopover(d) {

    var popuptext = "Adset ID: " + d.adset_id;
  
    $(this).popover({
        title: 'Campaign ID: ' + d.campaign_id,
        container: '#lchart',
        placement: 'auto',
        selector: ".linePoint",
        animation:true,
        trigger: 'manual',
        html: true,
        content: function() {
            return "Daily Budget: " + d.daily_budget + '\n' + "Adset ID: " + d.adset_id;
        }
    });
    $(this).popover('show');
}