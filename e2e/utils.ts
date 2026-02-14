import { Page } from '@playwright/test';

export interface ProductData {
  genre: string;
  product_name: string;
  maker_name: string;
  reference_price: string;
  price_with_tax: string;
  base_price: string;
}

export async function fillForm(page: Page, data: Partial<ProductData>) {
  if (data.genre !== undefined) {
    await page.fill('#genre', data.genre);
  }
  if (data.product_name !== undefined) {
    await page.fill('#product_name', data.product_name);
  }
  if (data.maker_name !== undefined) {
    await page.fill('#maker_name', data.maker_name);
  }
  if (data.reference_price !== undefined) {
    await page.fill('#reference_price', data.reference_price);
  }
  if (data.price_with_tax !== undefined) {
    await page.fill('#price_with_tax', data.price_with_tax);
  }
  if (data.base_price !== undefined) {
    await page.fill('#base_price', data.base_price);
  }
}

export async function submitForm(page: Page) {
  await page.click('button.btn-generate');
}
