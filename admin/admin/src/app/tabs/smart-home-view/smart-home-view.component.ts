import { Component, Input } from '@angular/core';
import { Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'app-smart-home-view',
  standalone: true,
  imports: [],
  templateUrl: './smart-home-view.component.html',
  styleUrl: './smart-home-view.component.scss'
})

export class SmartHomeViewComponent {
  @Input() smarthomedevices: object = {};
  @Output() newSmartHomeDeviceEvent: EventEmitter<string> = new EventEmitter<string>();

  addNewItem(value: string) {
    this.newSmartHomeDeviceEvent.emit(value);
  }
}
