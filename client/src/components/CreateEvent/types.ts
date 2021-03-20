export type InventoryChangeInput = {
  productId: number;
  value: number;
};

export type EventInput = {
  eventType: string;
  storeId?: number;
  description?: string;
  inventorychangeSet: InventoryChangeInput[];
};
