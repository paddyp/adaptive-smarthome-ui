import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SmTableComponent } from './sm-table.component';

describe('SmTableComponent', () => {
  let component: SmTableComponent;
  let fixture: ComponentFixture<SmTableComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [SmTableComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(SmTableComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
