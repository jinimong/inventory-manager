export type OptionType = {
  label: string;
  value: string | number;
  __isNew__?: boolean;
};

export enum EventType {
  SELL_DIRECT = 'SD',
  ORDER_PRODUCT = 'OP',
  SEND_PRODUCT = 'SP',
  SETTLE_SALE = 'SS',
  LEAVE_STORE = 'LS',
  DEFECT_PRODUCT_IN_STORE = 'DS',
  DEFECT_PRODUCT_IN_HOME = 'DH',
}

export const EventTypeMap = new Map([
  [EventType.SELL_DIRECT, '개인판매'],
  [EventType.ORDER_PRODUCT, '제품발주'],
  [EventType.SEND_PRODUCT, '입점처 입고'],
  [EventType.SETTLE_SALE, '판매내역정산'],
  [EventType.LEAVE_STORE, '입점처 퇴점'],
  [EventType.DEFECT_PRODUCT_IN_STORE, '불량:입점처'],
  [EventType.DEFECT_PRODUCT_IN_HOME, '불량:집'],
]);

export const eventTypesAboutStore = [
  EventType.SEND_PRODUCT,
  EventType.SETTLE_SALE,
  EventType.LEAVE_STORE,
  EventType.DEFECT_PRODUCT_IN_STORE,
];

export const eventTypesDecreaseFromStore = [
  EventType.SETTLE_SALE,
  EventType.LEAVE_STORE,
  EventType.DEFECT_PRODUCT_IN_STORE,
];
