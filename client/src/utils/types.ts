export type ProductMaterial = {
  id: number;
  name: string;
};

export type ProductCategory = {
  id: number;
  name: string;
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
};

export type InventoryChange = {
  id: number;
  product: Product;
  count: number;
};

export type Store = {
  id: number;
  name: string;
  description: string;
  eventSet: Event[];
};

export type StoreProduct = {
  store: Store;
  product: Product;
  count: number;
};

export type Event = {
  id: number;
  eventType: string;
  createdAt: string;
  updatedAt: string;
  description: string;
  store: Store;
  inventorychangeSet: InventoryChange[];
};
