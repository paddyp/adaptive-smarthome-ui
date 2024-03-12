import { Component, EventEmitter, Input, Output } from '@angular/core';
import { UIElement } from '../interfaces/uielement';
@Component({
  selector: 'app-base-component',
  standalone: false,
  // imports: [],
  template: "",
  // templateUrl: './base-component.component.html',
  styles: ""
  // styleUrl: './base-component.component.scss'
})
export class BaseComponentComponent {
  @Input() data!: UIElement;
  @Output() updateEvent: EventEmitter<object> = new EventEmitter<object>();

  sendChangedValues(event: any): void {
    // ToDo: Implement send to Server
    let payload = {
      "method": "update",
      "type": "data",
      "data": event.data
    }
    this.updateEvent.emit(payload);
  }

}
