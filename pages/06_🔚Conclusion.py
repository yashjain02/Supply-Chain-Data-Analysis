import streamlit as st

st.title('Conclusion On the Analysis')

with st.expander("👥️ -Customer Report ", expanded=False):
    st.write(
        """    
- 1:
    -Give More priority to customer Id 5654 and 2641 because they have puchased more and given a good profit."""
    )
    st.write(
        """    
- 2:
    -Avoid given item to the customer starting name with Mary because they have done many fraud transaction."""
    )
    st.write(
        """    
- 3:
    -Make a discounted plan for customer who are working from home because they have given the least order"""
    )
with st.expander("🛒 -Order Report ", expanded=False):
    st.write(
        """- 1: -Most purchased items where men's footwear, fishing equipments, gym equipments. So customer who are 
        sports and gym enthusiast have puschased more. And mostly they are from Central America and western Europe """
    )
with st.expander("🚚 -Delivery Report ", expanded=False):
    st.write(
        """- 1: -Should improve delivery in canada,South Africa and central Asia because they have received late 
        deliveries or shipping got cancelled """
    )
    st.write(
        """- 2: -Most of time were late deliveries """
    )
with st.expander("💵 -Sales Report ", expanded=False):
    st.write(
        """- 1: -2018 had the least sales compared to previous years """
    )
    st.write(
        """- 2: -Most sales were done in quarter 3 especially in month of september and october"""
    )
with st.expander("💰 -Profit Report ", expanded=False):
    st.write(
        """- 1: -Shoes and women's Accessories and given more profit in region central america and western europe """
    )
with st.expander("🌏 -Geographic Report ", expanded=False):
    st.write(
        """- 1: -Overall profit comes from Indonesia and Australia """
    )
    st.write(
        """- 2: -Customer from US tend to do more fraud transactions"""
    )



