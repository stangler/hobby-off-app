import { test, expect } from '@playwright/test';

test.describe('Form Validation', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('http://localhost:3000');
  });

  test('should show validation error when required fields are empty', async ({ page }) => {
    // Clear a required field
    const genreInput = page.locator('#genre');
    await genreInput.clear();
    
    // Attempt to submit
    await page.click('button.btn-generate');

    // Check if the field is invalid (HTML5 validation)
    const isValid = await genreInput.evaluate((el: HTMLInputElement) => el.checkValidity());
    expect(isValid).toBe(false);

    // Ensure preview is not shown
    const preview = page.locator('#preview');
    await expect(preview).not.toBeVisible();
  });

  test('all required fields should have required attribute', async ({ page }) => {
    const requiredFields = [
      '#genre',
      '#product_name',
      '#maker_name',
      '#reference_price',
      '#price_with_tax',
      '#base_price'
    ];

    for (const selector of requiredFields) {
      const input = page.locator(selector);
      await expect(input).toHaveAttribute('required', '');
    }
  });
});
