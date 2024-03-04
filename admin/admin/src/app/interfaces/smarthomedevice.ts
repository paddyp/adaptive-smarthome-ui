export interface SmartHomeDeviceChannel {
    channel_no: number;
    type: string;
}
export interface SmarthomeDevice {
    name: string;
    icon: string;
    id: number;
    channels: [SmartHomeDeviceChannel]
}