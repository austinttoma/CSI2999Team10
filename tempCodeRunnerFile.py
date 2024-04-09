    if request.method == 'POST':
        recycle_item = request.form['recycle']
        current_count = recycle_track_ref.val()[user_key].get(recycle_item)
        new_count = recycle_track_ref.val()[user_key].get(recycle_item)
        new_count = current_count + 1
        db.child('recycleTrack').child(user_key).update({recycle_item: new_count})
        return redirect(url_for('recycletracker'))

    return render_template('recycletracker.html', water_count=water_count, cans_count=cans_count)