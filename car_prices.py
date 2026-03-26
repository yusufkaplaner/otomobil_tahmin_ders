import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score
from mpl_toolkits.mplot3d import Axes3D # 3D için gerekli

# 1. Veriyi yükle
df = pd.read_excel('CarSales.xlsx')
df.columns = df.columns.str.strip()

# Sütun adındaki 's' harfini unutmadık :)
target_col = 'Price_in_thousands' 
df = df.dropna(subset=['Horsepower', target_col, 'Engine_size', 'Curb_weight'])

# Değişkenleri ata
X = df[['Horsepower']].values
y = df[target_col].values
X_multi = df[['Horsepower', 'Engine_size', 'Curb_weight']].values

results = []

def evaluate_model(name, y_true, y_pred):
    mse = mean_squared_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)
    results.append({'Model': name, 'MSE': mse, 'R2': r2})

# --- A. BASİT DOĞRUSAL ---
model_simple = LinearRegression().fit(X, y)
y_pred_simple = model_simple.predict(X)
evaluate_model("Simple Linear", y, y_pred_simple)

plt.figure(figsize=(6,4))
plt.scatter(X, y, color='blue', alpha=0.5, label='Gerçek Veriler')
plt.plot(X, y_pred_simple, color='red', label='Tahmin Çizgisi')
plt.title('A. Basit Doğrusal Regresyon')
plt.legend(); plt.show()

# --- B. ÇOKLU DOĞRUSAL (Normal ve 3D Grafik) ---
model_multi = LinearRegression().fit(X_multi, y)
y_pred_multi = model_multi.predict(X_multi)
evaluate_model("Multiple Linear", y, y_pred_multi)

# B1: Normal Hata Grafiği
plt.figure(figsize=(6,4))
plt.scatter(y, y_pred_multi, color='purple', alpha=0.5)
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=2)
plt.title('B. Çoklu Doğrusal Regresyon (Gerçek vs Tahmin)')
plt.show()

# B2: HAVALI 3D GRAFİK (Horsepower, Engine_size, Price)
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(df['Horsepower'], df['Engine_size'], y, color='blue', alpha=0.4)

# Tahmin düzlemi
hp_range = np.linspace(df['Horsepower'].min(), df['Horsepower'].max(), 20)
eng_range = np.linspace(df['Engine_size'].min(), df['Engine_size'].max(), 20)
hp_grid, eng_grid = np.meshgrid(hp_range, eng_range)

# Düzlem tahmini için Curb_weight'i sabit (ortalama) alıyoruz
curb_mean = df['Curb_weight'].mean()
z_pred = model_multi.predict(np.c_[hp_grid.ravel(), eng_grid.ravel(), np.full(hp_grid.ravel().shape, curb_mean)])
z_pred = z_pred.reshape(hp_grid.shape)

ax.plot_surface(hp_grid, eng_grid, z_pred, color='red', alpha=0.2)
ax.set_xlabel('Horsepower'); ax.set_ylabel('Engine Size'); ax.set_zlabel('Price')
plt.title('B. Çoklu Regresyon - 3D Tahmin Düzlemi')
plt.show()

# --- C. POLİNOMİYAL (Degree=3) ---
poly = PolynomialFeatures(degree=3)
X_poly = poly.fit_transform(X)
model_poly = LinearRegression().fit(X_poly, y)
y_pred_poly = model_poly.predict(X_poly)
evaluate_model("Polynomial (Deg:3)", y, y_pred_poly)

X_grid = np.linspace(X.min(), X.max(), 100).reshape(-1, 1)
plt.figure(figsize=(6,4))
plt.scatter(X, y, color='blue', alpha=0.5)
plt.plot(X_grid, model_poly.predict(poly.fit_transform(X_grid)), color='green', lw=2)
plt.title('C. Polinomiyal Regresyon (Deg=3)')
plt.show()

# --- D. RIDGE REGRESYON ---
model_ridge = Ridge(alpha=1.0).fit(X_multi, y)
y_pred_ridge = model_ridge.predict(X_multi)
evaluate_model("Ridge Regression", y, y_pred_ridge)

plt.figure(figsize=(6,4))
plt.scatter(y, y_pred_ridge, color='orange', alpha=0.5)
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=2)
plt.title('D. Ridge Regresyon (Alpha=1.0)')
plt.show()

# --- SONUÇ TABLOSU ---
print("\n" + "="*45)
print(f"{'YUSUF KAPLANER - ÖDEV SONUÇLARI':^45}")
print("="*45)
print(f"{'Model Türü':<20} | {'MSE':<10} | {'R-Squared':<10}")
print("-"*45)
for res in results:
    print(f"{res['Model']:<20} | {res['MSE']:<10.2f} | {res['R2']:<10.4f}")