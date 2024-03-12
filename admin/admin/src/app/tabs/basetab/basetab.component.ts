import { Component, EventEmitter, Input, Output } from '@angular/core';

@Component({
  selector: 'app-basetab',
  standalone: false,
  template: "",
  styles: "",

})
export class BasetabComponent {
  @Input() data: any;
  @Input() schema: any;
  editID: number = -1;
  @Output() updateEvent: EventEmitter<object> = new EventEmitter<object>();
  BASE_INFORMATION: object = {};
  createData = {};
  type!: string;

  toggleEditMode(item: number) {
    if (item == this.editID) {
      this.editID = -1;
    } else {
      this.editID = item;
    }
  }

  Submit(event: any): void {
    let updatePayload = {};
    if (!event.hasOwnProperty('id')) {
      updatePayload = {
        "method": "create",
        "type": this.type,
        "data": event
      }
    } else {
      updatePayload = {
        "method": "update",
        "type": this.type,
        "data": event
      }
    }
    console.log(JSON.stringify(updatePayload))
    this.updateEvent.emit(updatePayload);
    this.createData = JSON.parse(JSON.stringify(this.BASE_INFORMATION))
  }

  deleteItem(item: object) {
    // this.newSmartHomeDeviceEvent.emit(value);
    let deletePayload = {
      "method": "delete",
      "type": this.type,
      "data": item
    }
    this.updateEvent.emit(deletePayload);
  }

}
