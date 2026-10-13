import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(page_title="Quản lý điểm sinh viên", page_icon="🎓", layout="wide")

# Thay bằng thông tin của bạn
HO_TEN_NGUOI_TAO = "[VŨ NAM HẢI]"
MSSV_NGUOI_TAO = "033208013470]"

# 1. Dữ liệu 10 sinh viên
raw_data = {
    "Họ tên": ["Nguyễn Văn An", "Trần Thị Bình", "Lê Hoàng Cường", "Phạm Thị Dung", "Hoàng Tiến Dũng",
        "Ngô Thị Phương", "Vũ Đình Giang", "Đỗ Thị Hoa", "Bùi Văn Hùng", "Trương Thị Linh"],
    "Chuyên cần": [9.0, 8.0, 10.0, 6.0, 7.0, 9.0, 8.0, 5.0, 10.0, 7.0],
    "Giữa kỳ": [8.5, 7.0, 6.5, 9.0, 5.5, 8.0, 9.5, 7.5, 6.0, 8.5],
    "Cuối kỳ": [9.0, 8.0, 9.0, 4.0, 7.0, 8.0, 6.0, 3.0, 10.0, 7.0],
}
df = pd.DataFrame(raw_data)

# 2. Tính điểm tổng kết
df["Tổng kết"] = (
    df["Chuyên cần"] * 0.2
    + df["Giữa kỳ"] * 0.3
    + df["Cuối kỳ"] * 0.5
).round(2)

# 3. Xếp loại sinh viên
def xep_loai(diem):
    if diem >= 8.5:
        return "Giỏi"
    elif diem >= 7:
        return "Khá"
    elif diem >= 5:
        return "Trung bình"
    return "Yếu"

df["Xếp loại"] = df["Tổng kết"].apply(xep_loai)

st.title("QUẢN LÝ ĐIỂM SINH VIÊN")
st.write("Ứng dụng thống kê và trực quan hóa kết quả học tập của 10 sinh viên.")

st.subheader("1. Bảng điểm của 10 sinh viên")
st.dataframe(df, use_container_width=True, hide_index=True)

# 4. Thống kê
st.subheader("2. Thống kê kết quả học tập")
diem_tb = df["Tổng kết"].mean()
sv_cao_nhat = df.loc[df["Tổng kết"].idxmax()]
sv_thap_nhat = df.loc[df["Tổng kết"].idxmin()]
so_sv_dat = (df["Tổng kết"] >= 5).sum()

col1, col2, col3, col4 = st.columns(4)
col1.metric("Điểm trung bình lớp", f"{diem_tb:.2f}")
col2.metric("Điểm cao nhất", f"{sv_cao_nhat["Tổng kết"]:.2f}", help=f"Sinh viên: {sv_cao_nhat["Họ tên"]}")
col3.metric("Điểm thấp nhất", f"{sv_thap_nhat["Tổng kết"]:.2f}", help=f"Sinh viên: {sv_thap_nhat["Họ tên"]}")
col4.metric("Số sinh viên đạt", f"{so_sv_dat}/{len(df)}")

st.write(f"**Sinh viên có điểm tổng kết cao nhất:** {sv_cao_nhat["Họ tên"]} ({sv_cao_nhat["Tổng kết"]:.2f} điểm)")
st.write(f"**Sinh viên có điểm tổng kết thấp nhất:** {sv_thap_nhat["Họ tên"]} ({sv_thap_nhat["Tổng kết"]:.2f} điểm)")

# 5. Selectbox chọn sinh viên
st.subheader("3. Tra cứu điểm của sinh viên")
ten_chon = st.selectbox("Chọn sinh viên:", df["Họ tên"].tolist())
sv = df.loc[df["Họ tên"] == ten_chon].iloc[0]
st.write(f"**Họ tên:** {sv["Họ tên"]}")
st.write(f"**Điểm chuyên cần:** {sv["Chuyên cần"]}")
st.write(f"**Điểm giữa kỳ:** {sv["Giữa kỳ"]}")
st.write(f"**Điểm cuối kỳ:** {sv["Cuối kỳ"]}")
st.write(f"**Điểm tổng kết:** {sv["Tổng kết"]:.2f}")
st.write(f"**Xếp loại:** {sv["Xếp loại"]}")

# 6. Biểu đồ cột ngang
st.subheader("4. Biểu đồ điểm tổng kết của 10 sinh viên")
fig, ax = plt.subplots(figsize=(10, 6))
ax.barh(df["Họ tên"], df["Tổng kết"], color="cornflowerblue")
ax.set_title("Điểm tổng kết của 10 sinh viên")
ax.set_xlabel("Điểm tổng kết")
ax.set_ylabel("Tên sinh viên")
ax.set_xlim(0, 10)
ax.invert_yaxis()
ax.grid(axis="x", alpha=0.2)
ax.set_axisbelow(True)
fig.tight_layout()
st.pyplot(fig)
plt.close(fig)

# 7. Thông tin người tạo ứng dụng
st.divider()
st.caption(f"Người tạo ứng dụng: {HO_TEN_NGUOI_TAO} | MSSV: {MSSV_NGUOI_TAO}")
