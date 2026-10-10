import streamlit as st
from datetime import date

st.set_page_config(page_title="Billing", page_icon="🧾", layout="centered")

st.markdown(
    """
    <style>
    #MainMenu, footer, header {visibility: hidden;}
    .block-container {padding-top: 2rem; max-width: 460px;}
    .card {
        background: #ffffff; border: 1px solid #eef0f3;
        border-radius: 14px; padding: 14px 16px; margin-top: 12px;
        color: #1f2937;
    }
    .row {display: flex; justify-content: space-between; padding: 5px 0;
          font-size: 15px; color: #6b7280;}
    .row b {color: #1f2937; font-weight: 500;}
    .opt-title {font-size: 13px; color: #9ca3af; margin-bottom: 4px;}
    .total {font-size: 26px; font-weight: 600; color: #1f2937;}
    </style>
    """,
    unsafe_allow_html=True,
)

ONU_DEPOSIT = 500

st.markdown("### Billing")

connection_date = st.date_input(
    "Connection date",
    value=date.today(),
    min_value=date(2020, 1, 1),
    max_value=date(2035, 12, 31),
    format="DD-MM-YYYY",
)
package = st.number_input("Package (Tk)", min_value=0, value=0, step=50)

if st.button("Calculate", use_container_width=True):
    if package <= 0:
        st.warning("Package amount likho.")
    else:
        running_days = max(0, 30 - connection_date.day + 1)
        running_month = running_days * (package / 30)
        option1 = running_month + ONU_DEPOSIT
        option2 = running_month + package + ONU_DEPOSIT

        st.markdown(
            f"""
            <div class="card">
              <div class="row">Connection date<b>{connection_date.strftime('%d-%m-%Y')}</b></div>
              <div class="row">Running days<b>{running_days} days</b></div>
              <div class="row">Running month<b>{running_month:.0f} Tk</b></div>
              <div class="row">ONU deposit<b>{ONU_DEPOSIT} Tk</b></div>
            </div>
            <div class="card">
              <div class="opt-title">Option 1 · Running + ONU</div>
              <div class="total">{option1:.0f} Tk</div>
            </div>
            <div class="card">
              <div class="opt-title">Option 2 · Running + 1 month advance + ONU</div>
              <div class="total">{option2:.0f} Tk</div>
              <div class="row">Advance<b>{package} Tk</b></div>
            </div>
            """,
            unsafe_allow_html=True,
        )
