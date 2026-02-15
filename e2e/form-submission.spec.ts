import { test, expect } from '@playwright/test';
import { fillForm, submitForm, ProductData } from './utils';

test.describe('Form Submission', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('http://localhost:3000');
  });

  test('should successfully generate an image with valid input', async ({ page }) => {
    test.setTimeout(90000);

    const testData: ProductData = {
      genre: 'トレーディングカード',
      product_name: 'リザードンVMAX', // title → product_name に修正
      maker_name: 'ポケモン',
      reference_price: '5,000',
      price_with_tax: '4,400',
      base_price: '4,000',
    };

    await fillForm(page, testData);
    await submitForm(page);

    // Check if loading message appeared
    await expect(page.locator('#loading')).toBeVisible();

    // ローディングが消えるのを待つ
    await expect(page.locator('#loading')).toBeHidden({ timeout: 60000 });

    // エラーメッセージが表示されていないか確認
    const errorMessage = page.locator('.error-message, #error, [role="alert"]');
    const hasError = await errorMessage.isVisible().catch(() => false);
    if (hasError) {
      const errorText = await errorMessage.textContent();
      throw new Error(`API Error detected: ${errorText}`);
    }

    // プレビュー画像のsrc属性が設定されるのを待つ
    const previewImage = page.locator('#previewImage');
    await expect(previewImage).toHaveAttribute('src', /^blob:/, { timeout: 15000 });
    
    // 画像が実際に表示されるのを待つ
    await expect(previewImage).toBeVisible({ timeout: 5000 });

    // プレビュー要素が表示されることを確認
    const preview = page.locator('#preview');
    await expect(preview).toBeVisible();

    // Check if download button is available
    const downloadBtn = page.getByRole('button', { name: '画像をダウンロード' });
    await expect(downloadBtn).toBeVisible();
  });

  test('should reset form fields when reset button is clicked', async ({ page }) => {
    // Modify a field
    await page.fill('#genre', 'Modified Genre');
    
    // Click reset
    await page.click('button.btn-reset');

    // Wait for the reset logic (setTimeout(..., 0) in form.html)
    await page.waitForTimeout(100);

    // Check if it returned to default values defined in the script
    await expect(page.locator('#genre')).toHaveValue('プラモデル');
    await expect(page.locator('#product_name')).toHaveValue('ガンダムRX-78-2');
  });
});