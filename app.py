import streamlit as st
import plotly.express as px
from PIL import Image
import time

# ==============================================================================
# 1. KONFIGURASI HALAMAN UTAMA
# ==============================================================================
st.set_page_config(
    page_title="Safety Culture - Mode Live",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown(
    """
    <style>
    .block-container {
        padding-top: 1.0rem !important; 
        max-width: 95% !important;
    }
    .custom-title {
        font-size: 32px !important; 
        font-weight: 600 !important;
        color: #1E293B;
        margin-top: 20px; 
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Layout untuk tombol dan judul
col_btn, col_title = st.columns([1.5, 3])

with col_btn:
    # Tombol HTML Manual agar ukuran font dan tombol bisa dipaksa membesar
    st.markdown("""
        <a href="https://forio.com/app/bustamiizhari/culture" target="_blank" 
           style="
            display: inline-block;
            background: linear-gradient(135deg, #1E3A8A 0%, #3B82F6 100%);
            color: #FFFFFF;
            padding: 20px 40px;
            font-size: 35px;
            font-weight: bold;
            border-radius: 12px;
            text-decoration: none;
            box-shadow: 0 4px 12px rgba(59, 130, 246, 0.5);
            text-align: center;
            border: none;
        ">
        🏠 Simulation Open Here
        </a>
    """, unsafe_allow_html=True)

with col_title:
    st.markdown('<p class="custom-title">Lack of Safety Culture leads to high cost</p>', unsafe_allow_html=True)

st.divider()

# ==============================================================================
# 4. MEMUAT BACKGROUND IMAGE
# ==============================================================================
try:
    img = Image.open("culture.png") 
except FileNotFoundError:
    st.error("File 'culture.png' tidak ditemukan.")
    st.stop()

# ==============================================================================
# 5. DATA KOORDINAT XY
# ==============================================================================
process_phases = [
    [{'label': '', 'shape_type': 'rect', 'is_bottom': False, 'tank_area': [304,36, 506, 108]},
     {'label': '', 'shape_type': 'rect', 'is_bottom': False, 'tank_area': [874, 41,1082 ,114 ]}],
    [{'label': '', 'shape_type': 'rect', 'is_bottom': False, 'tank_area': [18, 387, 163, 452]},
     {'label': '', 'shape_type': 'rect', 'is_bottom': False, 'tank_area': [1275,131,1435,205]},
     {'label': '', 'shape_type': 'rect', 'is_bottom': False, 'tank_area': [539,458, 720, 538]},
     {'label': '', 'shape_type': 'rect', 'is_bottom': False, 'tank_area': [1462, 422, 1659, 462]},
     {'label': '', 'shape_type': 'rect', 'is_bottom': False, 'tank_area': [1018, 490, 1209, 569]}],
    [{'label': '', 'shape_type': 'rect', 'is_bottom': False, 'tank_area': [582, 224, 796, 341]},
     {'label': '', 'shape_type': 'rect', 'is_bottom': False, 'tank_area': [854, 224, 1037, 341]}],
]

# ==============================================================================
# 6. RENDERING LOGIC
# ==============================================================================
placeholder = st.empty()
render_count = 0

while True:
    active_components = []
    for phase in process_phases:
        active_components.extend(phase)
        fig = px.imshow(img)
        fig.update_xaxes(visible=False, showgrid=False)
        fig.update_yaxes(visible=False, showgrid=False)
        
        for component in active_components:
            area = component['tank_area']
            fig.add_shape(type="rect", x0=area[0], y0=area[1], x1=area[2], y1=area[3],
                          fillcolor="rgba(212, 175, 55, 0.35)", line=dict(width=0))
        
        # Tinggi grafik ditingkatkan ke 850 agar tampilan lebih besar
        fig.update_layout(margin=dict(l=0, r=0, t=0, b=0), height=850, showlegend=False)
        
        with placeholder.container():
            st.plotly_chart(fig, use_container_width=True, key=f"key_{render_count}")
        
        render_count += 1
        time.sleep(3.0)
