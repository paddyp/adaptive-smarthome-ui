import { ComponentFixture, TestBed } from '@angular/core/testing';

import { FormularBuilderComponent } from './formular-builder.component';

describe('FormularBuilderComponent', () => {
  let component: FormularBuilderComponent;
  let fixture: ComponentFixture<FormularBuilderComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [FormularBuilderComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(FormularBuilderComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
