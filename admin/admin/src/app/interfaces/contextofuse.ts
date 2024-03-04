export enum TypeEnum {
    INT = 'INT',
    FLOAT = 'FLOAT',
    STRING = 'STRING',
    JSON = 'JSON',
    DEVICE = 'DEVICE'
}

export interface Contextofuse {
    key: string;
    value: string;
    type: TypeEnum;
    smarthomedevicechannel_id: number;

}
