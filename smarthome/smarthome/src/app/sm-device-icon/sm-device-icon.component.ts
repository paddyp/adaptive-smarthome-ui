import { Component, Input } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-sm-device-icon',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './sm-device-icon.component.html',
  styleUrl: './sm-device-icon.component.scss'
})
export class SmDeviceIconComponent {
  @Input("icon") iconName = '';
}
