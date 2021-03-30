import { EventType } from './common';

export type ProductMaterial = {
  id: number;
  name: string;
};

export type ProductCategory = {
  id: number;
  name: string;
};

export type ProductImage = {
  photo: string;
  photoThumbnail: string;
};

export type Product = {
  id: number;
  name: string;
  barcode: string;
  description: string;
  materials: ProductMaterial[];
  categories: ProductCategory[];
  price: number;
  priceWithPees: number;
  count: number;
  archived: boolean;
  storeProducts: StoreProduct[];
  images: ProductImage[];
};

export type InventoryChange = {
  id: number;
  product: Product;
  value: number;
};

export type Store = {
  id: number;
  name: string;
  description: string;
  storeProducts: StoreProduct[];
  eventSet: Event[];
};

export type StoreProduct = {
  id: number;
  store: Store;
  product: Product;
  count: number;
};

export type Event = {
  id: number;
  eventType: EventType;
  createdAt: string;
  updatedAt: string;
  description: string;
  store: Store;
  inventoryChanges: InventoryChange[];
};
