export enum ActionEnum {
    ADDVIEWCOMPONENT = 'ADDVIEWCOMPONENT',
    DELETEVIEWCOMPOENT = 'DELETEVIEWCOMPOENT',
    CREATEVIEWCOMPONENT = 'CREATEVIEWCOMPONENT',
    LAYOUTCHANGE = 'LAYOUTCHANGE',
    SETDISPLAYPROPERTY = 'SETDISPLAYPROPERTY',
    SERVICEFUNCTIONCALL = 'SERVICEFUNCTIONCALL'
}
export interface Action {
    adaptui_id: number;
    action: string;
}
export interface Adaptuirule {
    id: number;
    name: string;
    actionGroup: ActionEnum;
    actions: Array<Action>;


}
