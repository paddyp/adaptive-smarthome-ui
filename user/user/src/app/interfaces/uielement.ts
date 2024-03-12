export enum ElementsEnum {
    BUTTON = "BUTTON",
    TOGGLE_BUTTON = "TOGGLE_BUTTON",
    SLIDER = "SLIDER"
}

export enum TypeEnum {
    INT = "INT",
    FLOAT = "FLOAT"

}
export interface ContextOfUse {
    id: number
    key: string
    value: string
    type: TypeEnum
}

export interface Value {
    id: number
    name: string
    contextofuse: ContextOfUse
}

export interface UIElement {
    id: number
    uielement: ElementsEnum
    name: string
    current_value: number
    min: number
    max: number
    step: number
    min_color: string
    max_color: string
    values: [Value]
    description: string
    orderlevel: number

}
