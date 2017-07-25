def mesh_both_data(last_7_days, todays_data):
    final_dict={}
    all_collections=[]
    recid = 1
    if last_7_days:
        for items in last_7_days:
            all_collections.append({'recid': recid, 'date':items.date,'campaign_id':items.campaign_id,'adset_id':items.adset_id,'bid_amount': items.bid_avg_amount,\
            'daily_budget': items.daily_avg_budget})
            recid += 1
    if todays_data:
        for items in todays_data:
            all_collections.append({'recid': recid ,'date':items.date,'campaign_id':items.campaign_id,'adset_id':items.adset_id,'bid_amount': items.bid_amount,'daily_budget': items.daily_budget})
            recid += 1
    final_dict['data'] = all_collections
    return all_collections



		 
