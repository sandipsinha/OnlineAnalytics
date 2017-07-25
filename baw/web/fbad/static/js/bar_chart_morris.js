function initdbarChart(){
      return Morris.Bar({
      element: 'barChart',
      xkey: 'adset_id',
      ykeys: ['daily_budget','bid_amount'],
      labels: ['Series A','Series B']
    });
    
     

}
  