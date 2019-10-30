package com.example.etfrobotics;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

import helpers.MqttHelper;

public class MainActivity extends AppCompatActivity {
    MqttHelper mqttHelper;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        final Button button = findViewById(R.id.showHistory);
        button.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                Intent myIntent = new Intent(MainActivity.this, ShowChartsActivity.class);
                MainActivity.this.startActivity(myIntent);
            }
        });


    }


}
