import { Component, Input } from '@angular/core';
import { FormControl, ReactiveFormsModule } from '@angular/forms';
import { Bootstrap5FrameworkModule } from '@zajsf/bootstrap5';
import { CommonModule } from '@angular/common';
import { BasetabComponent } from '../basetab/basetab.component';

@Component({
  selector: 'app-smart-home-view',
  standalone: true,
  imports: [ReactiveFormsModule, Bootstrap5FrameworkModule, CommonModule],
  templateUrl: './smart-home-view.component.html',
  styleUrl: './smart-home-view.component.scss'
})

export class SmartHomeViewComponent extends BasetabComponent {
  override BASE_INFORMATION: object = { 'channels': [{ 'channel_no': 1 }] };
  override createData = JSON.parse(JSON.stringify(this.BASE_INFORMATION)) // copy object
  override type = "smarthomedevice";
}
