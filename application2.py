
# 変更後
data_load_state.text("Done! (using st.cache)")

st.subheader('Raw data')
st.write(data)

st.subheader('Number of pickups by hour')
hist_values = np.histogram(
    data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)


st.subheader('Map of all pickups')
st.map(data)

hour_to_filter = 17
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
st.subheader(f'Map of all pickups at {hour_to_filter}:00')
st.map(filtered_data)


# 変更後
hour_to_filter = st.slider('hour', 0, 23, 17)  # min: 0h, max: 23h, default: 17h


# 変更後
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)



